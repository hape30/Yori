export default function Tutorials() {
    return (
        <div className="max-w-4xl mx-auto mt-10">
            <h2 className="text-2xl font-bold mb-4">Обучающие материалы</h2>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="border p-4 rounded">Курс 1: Web Security Basics</div>
                <div className="border p-4 rounded">Курс 2: OWASP Top 10</div>
            </div>
        </div>
    );
}
