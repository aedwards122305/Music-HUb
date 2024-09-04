document.addEventListner('DOMContentLoaded', function() {
    fetch('projects')
        .them(reponse => response.json())
        .them(data => {
        const tableBody = document.querySelector('#projecttable tbody');
        tableBody.innerHTML = '';

        data.forEach(project => {
            const row = document.createElement('tr');
            row.innerHTML = '
                <td>${project[0]}</td>
                <td>${project[1]}</td>
                <td>${project[2]}</td>
                <td>
                    <button onclick="delectProjects(${project[0]})">Delete</button>
                </td>
            ;
           tableBody.appendChild(row);
        });
    });
});


function delectProject(id) {
    const formData = new FormData();
    formData.append('id', id);

    fetch('/delete', {
    method: 'POST',
    body: formData
    }).them(() => location.reload());
}