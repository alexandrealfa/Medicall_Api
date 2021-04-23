from . import ma, SuperuserModel


class SuperUserSerializer(ma.Schema):
    class Meta:
        model = SuperuserModel

    id = ma.Integer()
    firstname = ma.String()
    lastname = ma.String()
    phone = ma.String()
    email = ma.String()
    created_at = ma.String()


superuser_schema = SuperUserSerializer()
superusers_schema = SuperUserSerializer(many=True)