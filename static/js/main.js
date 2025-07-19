document.addEventListener('DOMContentLoaded', function () {
    const input = document.getElementById('creator-input');
    const suggestions = document.getElementById('suggestions');

    input.addEventListener('input', function () {
        const query = input.value.trim();
        if (!query) {
            suggestions.style.display = 'none';
            suggestions.innerHTML = '';
            return;
        }

        fetch(`/autocomplete/?q=${encodeURIComponent(query)}`)
            .then(response => response.json())
            .then(data => {
                suggestions.innerHTML = '';
                if (data.results.length > 0) {
                    data.results.forEach(username => {
                        const li = document.createElement('li');
                        li.textContent = username;
                        li.style.padding = '4px';
                        li.style.cursor = 'pointer';
                        li.addEventListener('click', function () {
                            input.value = username;
                            suggestions.style.display = 'none';
                        });
                        suggestions.appendChild(li);
                    });
                    suggestions.style.display = 'block';
                } else {
                    suggestions.style.display = 'none';
                }
            });
    });

    document.addEventListener('click', function (e) {
        if (!suggestions.contains(e.target) && e.target !== input) {
            suggestions.style.display = 'none';
        }
    });

    
});


