export default function ViewPost() {
    return (
        <div className="max-w-4xl mx-auto mt-8 space-y-6">
            <div>
                <h1 className="text-2xl font-bold">Название проекта</h1>
                <p className="text-gray-600">Описание проекта, ссылка и аспекты для проверки...</p>
            </div>
            <div>
                <h2 className="text-xl font-semibold">Ответы</h2>
                {/* Список ответов */}
                <div className="border p-4 rounded mt-4">
                    <p><strong>Специалист:</strong> username</p>
                    <p>Здесь будет markdown-контент ответа</p>
                    <button className="mt-2 bg-yellow-500 text-white px-4 py-1 rounded">Оценить ответ</button>
                </div>
                {/* Форма нового ответа */}
                <form className="mt-6 space-y-3">
                    <textarea className="w-full p-2 border rounded" placeholder="Напишите рекомендацию... (Markdown поддерживается)" />
                    <input type="file" className="w-full p-2 border rounded" />
                    <button type="submit" className="bg-blue-600 text-white px-4 py-2 rounded">Отправить ответ</button>
                </form>
            </div>
        </div>
    );
}
