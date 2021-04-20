from http import HTTPStatus

from flask_restful import reqparse, request
from flask_jwt_extended import jwt_required

from sqlalchemy.exc import IntegrityError

from . import (BaseView, DoctorModel, EpisodeModel, PatientModel,
               doctors_schema, episodes_schema, patients_schema, superuser_schema, superusers_schema,
               SuperuserModel, is_bad_request, db_manager)


class SuperUser(BaseView):
    @jwt_required()
    def get(self):
        if self.get_type() != "superuser":
            return {"message": "Not Access"}, HTTPStatus.NOT_ACCEPTABLE
        superuser_id = self.get_id()
        current_superuser = SuperuserModel.query.get_or_404(superuser_id)
        serializer = superuser_schema.dump(current_superuser)

        return {"message": "success", "data": serializer}, HTTPStatus.OK

    def post(self):
        parse = reqparse.RequestParser()

        parse.add_argument("firstname", type=str, nullable=False),
        parse.add_argument("lastname", type=str, nullable=False),
        parse.add_argument("phone", type=str, nullable=False),
        parse.add_argument("email", type=str, nullable=False),
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

    @jwt_required()
    def patch(self):
        if self.get_type() != "superuser":
            return {"message": "Not Access"}, HTTPStatus.NOT_ACCEPTABLE
        parse = reqparse.RequestParser()

        parse.add_argument("firstname", type=str)
        parse.add_argument("lastname", type=str)
        parse.add_argument("phone", type=str)
        parse.add_argument("email", type=str)
        parse.add_argument("password", type=str)

        superuser_id = self.get_id()
        body = request.get_json()
        kwargs = parse.parse_args()
        current_superuser = SuperuserModel.query.get_or_404(superuser_id)

        if is_bad_request(body, kwargs.keys()):
            return {"message": "invalid values"}, HTTPStatus.BAD_REQUEST

        [
            setattr(current_superuser, key, value)
            for key, value in kwargs.items()
            if key != "password" and value is not None
        ]
        if kwargs.password:
            setattr(current_superuser, "password", kwargs.password)

        db_manager(current_superuser)
        serializer = superuser_schema.dump(current_superuser)

        return {"message": "success updated", "data": serializer}, HTTPStatus.OK

    @jwt_required()
    def delete(self):
        if self.get_type() != "superuser":
            return {"message": "Not Access"}, HTTPStatus.NOT_ACCEPTABLE
        superuser_id = self.get_id()
        current_superuser = SuperuserModel.query.get_or_404(superuser_id)
        db_manager(current_superuser, True)

        return {"message": f"patient {superuser_id} has been deleted"}, HTTPStatus.OK


class AllSuperUsers(BaseView):
    @jwt_required()
    def get(self):
        if self.get_type() != "superuser":
            return {"message": "Not Access"}, HTTPStatus.NOT_ACCEPTABLE

        all_superusers: SuperuserModel = SuperuserModel.query\
            .order_by(SuperuserModel.id)\
            .paginate(page=self.page_pagination(),
                      per_page=self.per_page_pagination(),
                      error_out=False).items

        serializer = superusers_schema.dump(all_superusers)

        return {"message": "success", "data": serializer}, HTTPStatus.OK


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