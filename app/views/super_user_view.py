from http import HTTPStatus

from flask_restful import reqparse, request
from flask_jwt_extended import jwt_required

from sqlalchemy.exc import IntegrityError

from . import (BaseView, DoctorModel, EpisodeModel, PatientModel,
               doctors_schema, episodes_schema, patients_schema,superuser_schema,
               SuperuserModel, is_bad_request, db_manager)


class SuperUser(BaseView):
    def post(self):
        parse = reqparse.RequestParser()

        parse.add_argument("firstname", type=str, nullable=False),
        parse.add_argument("lastname", type=str, nullable=False),
        parse.add_argument("phone", type=str, nullable=False),
        parse.add_argument("email", type=str, nullable=False, unique=True),
        parse.add_argument("password", type=str, nullable=False)

        kwargs = parse.parse_args()
        body = request.get_json()

        if is_bad_request(body, kwargs.keys()):
            return {"message": "invalid values"}, HTTPStatus.BAD_REQUEST

        new_super_user = SuperuserModel(**kwargs)

        try:
            db_manager(new_super_user)
        except IntegrityError:
            return {"message": "email already in use"}, HTTPStatus.NOT_ACCEPTABLE

        serializer = superuser_schema.dump(new_super_user)
        return {"message": "success created", "data": serializer}


class AllDoctors(BaseView):
    @jwt_required()
    def get(self):
        if self.get_type() != "superuser":
            return {"message": "Not Access"}, HTTPStatus.NOT_ACCEPTABLE

        all_doctors: DoctorModel = DoctorModel.query\
            .order_by(DoctorModel.id)\
            .paginate(page=self.page_pagination(),
                      per_page=self.per_page_pagination(),
                      error_out=False).items

        serializer = doctors_schema.dump(all_doctors)

        return {"message": "success", "data": serializer}, HTTPStatus.OK


class AllPatients(BaseView):
    @jwt_required()
    def get(self):
        if self.get_type() != "superuser":
            return {"message": "Not Access"}, HTTPStatus.NOT_ACCEPTABLE
        all_patients = PatientModel.query.\
            paginate(page=self.page_pagination(),
                     per_page=self.per_page_pagination(),
                     error_out=False).items

        serializer = patients_schema.dump(all_patients)
        return {"message": "success", "data": serializer}, HTTPStatus.OK


class AllEpisodes(BaseView):
    @jwt_required()
    def get(self):
        if self.get_type() != "superuser":
            return {"message": "Not Access"}, HTTPStatus.NOT_ACCEPTABLE
        all_episodes: EpisodeModel = EpisodeModel.query\
            .order_by(EpisodeModel.id)\
            .paginate(page=self.page_pagination(),
                      per_page=self.per_page_pagination,
                      error_out=False).items

        serializer = episodes_schema.dump(all_episodes)
        return {"message": "success", "data": serializer}, HTTPStatus.OK