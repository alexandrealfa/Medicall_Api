from . import db
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.exc import SQLAlchemyError


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)

    @declared_attr
    def __tablename__(cls):
        model_name = cls.__name__.replace("Model", "")
        plural_table_name = f"{model_name.lower()}s"
        return plural_table_name

    def save(self, deleted=False, auto_commit=True):

        # self.created_at = datetime.now(timezone.utc)
        db.session.add(self)
        if deleted:
            db.session.delete(self)
            db.session.commit()
        elif auto_commit:
            try:
                db.session.commit()
            except SQLAlchemyError as error:
                db.session.rollback()
                raise error