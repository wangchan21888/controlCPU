import os

# Định nghĩa cấu trúc thư mục
structure = {
    "cryptocurrency-website": {
        "model": {
            "cryptocurrency.js": """const cryptocurrencies = [
    { name: "Bitcoin", symbol: "BTC" },
    { name: "Ethereum", symbol: "ETH" },
    { name: "Ripple", symbol: "XRP" },
    { name: "Litecoin", symbol: "LTC" },
];

function getCryptocurrencies() {
    return cryptocurrencies;
}"""
        },
        "view": {
            "index.html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cryptocurrency Website</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Welcome to the World of Cryptocurrency</h1>
        <nav>
            <ul>
                <li><a href="#home">Home</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#cryptocurrencies">Cryptocurrencies</a></li>
                <li><a href="#news">News</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
        <button id="theme-toggle">Dark Mode</button>
    </header>

    <main>
        <section id="home">
            <h2>Home</h2>
            <p>Explore the world of cryptocurrency and the latest trends.</p>
        </section>

        <section id="about">
            <h2>About</h2>
            <p>Information about cryptocurrency and how it works.</p>
        </section>

        <section id="cryptocurrencies">
            <h2>Cryptocurrencies</h2>
            <div id="crypto-list"></div>
        </section>

        <section id="news">
            <h2>News</h2>
            <p>Stay updated with the latest news in the cryptocurrency field.</p>
        </section>

        <section id="contact">
            <h2>Contact</h2>
            <p>Our contact information.</p>
        </section>
    </main>

    <footer>
        <p>&copy; 2024 Cryptocurrency Website. All rights reserved.</p>
    </footer>

    <script src="../model/cryptocurrency.js"></script>
    <script src="../controller/script.js"></script>
</body>
</html>""",
            "styles.css": """body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    transition: background-color 0.3s, color 0.3s;
}

header {
    background-color: #4CAF50;
    color: white;
    padding: 10px 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

nav ul {
    list-style-type: none;
    padding: 0;
}

nav ul li {
    display: inline;
    margin-right: 20px;
}

nav a {
    color: white;
    text-decoration: none;
}

button {
    background-color: #fff;
    color: #4CAF50;
    border: none;
    padding: 10px 15px;
    cursor: pointer;
    border-radius: 5px;
    transition: background-color 0.3s;
}

button:hover {
    background-color: #e0e0e0;
}

main {
    padding: 20px;
}

footer {
    text-align: center;
    padding: 10px;
    background-color: #f1f1f1;
}

.dark-mode {
    background-color: #333;
    color: white;
}

.dark-mode header {
    background-color: #555;
}

.dark-mode nav a {
    color: #e0e0e0;
}"""
        },
        "controller": {
            "script.js": """const themeToggle = document.getElementById('theme-toggle');

themeToggle.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
    themeToggle.textContent = document.body.classList.contains('dark-mode') ? 'Light Mode' : 'Dark Mode';
});

function displayCryptocurrencies() {
    const cryptoList = getCryptocurrencies();
    const listContainer = document.getElementById('crypto-list');

    cryptoList.forEach(crypto => {
        const item = document.createElement('div');
        item.textContent = `${crypto.name} (${crypto.symbol})`;
        listContainer.appendChild(item);
    });
}

document.addEventListener('DOMContentLoaded', displayCryptocurrencies);"""
        }
    }
}

# Hàm tạo thư mục và file
def create_structure(structure):
    for folder, contents in structure.items():
        if not os.path.exists(folder):
            os.makedirs(folder)
        for name, content in contents.items():
            if isinstance(content, str):
                with open(os.path.join(folder, name), 'w', encoding='utf-8') as f:
                    f.write(content)

# Tạo cấu trúc thư mục
create_structure(structure)
print("Website structure created successfully!")
