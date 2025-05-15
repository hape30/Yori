import { Link } from 'react-router-dom';

export function Navbar({ user }) {
    return (
        <nav className="bg-gray-900 text-white p-4 flex justify-between">
            <div className="space-x-4">
                <Link to="/" className="font-bold">SafeCodeHub</Link>
                <Link to="/post">Создать запрос</Link>
                <Link to="/tutorials">Обучение</Link>
                <Link to="/forum">Форум</Link>
                <Link to="/leaderboard">Рейтинг</Link>
            </div>
            <div className="space-x-4">
                {user ? (
                    <Link to={`/profile/${user.id}`}>Профиль</Link>
                ) : (
                    <>
                        <Link to="/login">Вход</Link>
                        <Link to="/register">Регистрация</Link>
                    </>
                )}
            </div>
        </nav>
    );
}
