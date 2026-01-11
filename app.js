let sellers = [];

fetch("sellers.json")
    .then(res => res.json())
    .then(data => {
        sellers = data;
        renderTable(sellers);
    });

function renderTable(data) {
    const table = document.getElementById("sellerTable");
    table.innerHTML = "";

    data.forEach(seller => {
        const row = document.createElement("tr");

        row.innerHTML = `
            <td>${seller.type}</td>
            <td>
                ${seller.name}
                ${seller.verified ? "✅" : "⚠️"}
            </td>
            <td>
                <a href="${seller.catalog_url}" target="_blank">
                    ${seller.catalog_type.toUpperCase()}
                </a>
            </td>
            <td>${seller.known_for}</td>
            <td>${seller.quality_rating}</td>
            <td>${seller.price_rating}</td>
            <td>${seller.description}</td>
            <td>
                ${seller.contact_type === "whatsapp" ? "📱" : "<img width='15px' height='15px' src='https://img.icons8.com/?size=100&id=2mIgusGquJFz&format=png&color=000000'>"}
                ${seller.contact_value}
            </td>
        `;
        table.appendChild(row);
    });
}

// Filtres & tri
document.querySelectorAll("select").forEach(select => {
    select.addEventListener("change", applyFilters);
});

function applyFilters() {
    const type = document.getElementById("typeFilter").value;
    const catalog = document.getElementById("catalogFilter").value;
    const sort = document.getElementById("sortSelect").value;

    let filtered = [...sellers];

    if (type) filtered = filtered.filter(s => s.type === type);
    if (catalog) filtered = filtered.filter(s => s.catalog_type === catalog);

    filtered.sort((a, b) => {
        if (sort === "name") return a.name.localeCompare(b.name);
        return b[sort] - a[sort];
    });

    renderTable(filtered);
}