from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password):
        """ Creates a Normal User """
        if not email:
            raise ValueError("All Users must Have Email")
        user = self.model(
            email = self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
    def create_superuser(self, email, password):
        """ Creates a SuperUser ( Admin ) """
        user = self.model(
            email = self.normalize_email(email),
            staff = True,
            admin = True,
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
    def createConsumerUser(self, email, firstname, lastname, password):
        user = self.model(
            email = email,
            firstName = firstname,
            lastName = lastname,
            consumerUser = True,
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
