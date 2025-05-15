export default function Login({ setUser }) {
    return (
        <div className="max-w-md mx-auto mt-10">
            <h2 className="text-xl font-semibold mb-4">Вход</h2>
            <form className="space-y-4">
                <input type="email" placeholder="Email" className="w-full p-2 border rounded" />
                <input type="password" placeholder="Пароль" className="w-full p-2 border rounded" />
                <button type="submit" className="w-full bg-blue-600 text-white py-2 rounded">Войти</button>
            </form>
            <div className="mt-4 text-sm text-center">
                <p>Или войдите через:</p>
                <div className="flex justify-around mt-2">
                    <button className="bg-gray-800 px-3 py-1 text-white rounded">GitHub</button>
                    <button className="bg-blue-600 px-3 py-1 text-white rounded">Google</button>
                    <button className="bg-blue-800 px-3 py-1 text-white rounded">LinkedIn</button>
                </div>
            </div>
        </div>
    );
}
