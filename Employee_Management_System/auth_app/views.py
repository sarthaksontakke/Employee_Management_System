{% extends 'layouts/app.html'%}

{% block content%}
<h2>View All Employees</h2>
<hr>
<table class="table table-dark table-borderless" >
    <thead>
      <tr>
        <th scope="col">ID</th>
        <th scope="col">First Name</th>
        <th scope="col">Last Name</th>
        <th scope="col">Salary</th>
        <th scope="col">Bonus</th>
        <th scope="col">Phone Number</th>
        <th scope="col">Role</th>
        <th scope="col">Department</th>
        <th scope="col">Location</th>
        <th scope="col">Hire-date</th>
        <th scope="col">Actions</th>
      </tr>
    </thead>
    <tbody>
        {% for emp in emps %}
      <tr>
        <th scope="row">{{ emp.id }}</th>
        <td>{{ emp.first_name }}</td>
        <td>{{ emp.last_name }}</td>
        <td>{{ emp.salary }}</td>
        <td>{{ emp.bonus }}</td>
        <td>{{ emp.phone }}</td>
        <td>{{ emp.role.name }}</td>
        <td>{{ emp.dept.name }}</td>
        <td>{{ emp.dept.location }}</td>
        <td>{{ emp.hire_date }}</td>
        <td>
          <a href="{% url 'updateemp' emp.id %}" class="btn btn-sm btn-primary">Update</a>
          <a href="{% url 'deleteemployee' emp.id %}" class="btn btn-sm btn-danger">Delete</a>
        </td>
      </tr>
        {% endfor %}
    </tbody>
  </table>
{% endblock %}
