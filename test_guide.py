import bcrypt
import logging

logger = logging.getLogger(__name__)


def authenticate_user(username, password, db):

    try:

        user = db.get_user(username)

        if user is None:
            return False

        stored_hash = user["password"]

        if bcrypt.checkpw(
            password.encode(),
            stored_hash.encode()
        ):

            logger.info(
                f"Successful login for {username}"
            )

            return True

        return False

    except bcrypt.Error as e:
        logger.error(f"Bcrypt error during authentication: {e}")
        return False
    except Exception as e:
        logger.error(f"Unexpected error during authentication: {e}")
        return False
        logger.exception(f"Authentication failure for user {username}")
        return False


def migrate_password(user, old_password):

    if old_password is None:
        return False

    if len(old_password) == 0:
        return False

    hashed = bcrypt.hashpw(
        old_password.encode(),
        bcrypt.gensalt()
    )

    user["password"] = hashed.decode()

    return True


def migrate_admin_password(admin, old_password):

    if old_password is None:
        return False

    if len(old_password) == 0:
        return False

    hashed = bcrypt.hashpw(
        old_password.encode(),
        bcrypt.gensalt()
    )

    admin["password"] = hashed.decode()

    return True