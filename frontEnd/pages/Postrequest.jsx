export default function PostRequest() {
    return (
        <div className="max-w-2xl mx-auto mt-8 space-y-4">
            <h2 className="text-2xl font-bold">Создать запрос на аудит</h2>
            <form className="space-y-4">
                <input type="text" placeholder="Название проекта" className="w-full p-2 border rounded" />
                <textarea placeholder="Описание проекта" className="w-full p-2 border rounded h-32"></textarea>
                <input type="text" placeholder="Ссылка на репозиторий или демо" className="w-full p-2 border rounded" />
                <input type="file" className="w-full p-2 border rounded" />
                <input type="text" placeholder="Теги (через запятую)" className="w-full p-2 border rounded" />
                <button type="submit" className="w-full bg-indigo-600 text-white py-2 rounded">Опубликовать</button>
            </form>
        </div>
    );
}
