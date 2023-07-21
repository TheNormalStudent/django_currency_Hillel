from environs import Env


def get_username_and_password_for_settings() -> dict:
    env = Env()
    env.read_env()

    usrnm_pass = {'username': env.str('USERNAME'), 'password': env.str('PASSWORD')}

    return usrnm_pass
