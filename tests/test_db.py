from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):

    user = User(
        username='ducameneses',
        email='duca@gmail.com',
        password='minha_senha',
    )
    session.add(user)
    session.commit()

    result = session.scalar(
        select(User).where(User.email == 'duca@gmail.com')
    )

    assert result.id == 1
