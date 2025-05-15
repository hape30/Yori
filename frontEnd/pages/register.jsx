export default function Register() {
    return (
        <div className="max-w-md mx-auto mt-10">
            <h2 className="text-xl font-semibold mb-4">Регистрация</h2>
            <form className="space-y-4">
                <input type="text" placeholder="Имя пользователя" className="w-full p-2 border rounded" />
                <input type="email" placeholder="Email" className="w-full p-2 border rounded" />
                <input type="password" placeholder="Пароль" className="w-full p-2 border rounded" />
                <button type="submit" className="w-full bg-green-600 text-white py-2 rounded">Создать аккаунт</button>
            </form>
        </div>
    );
}
