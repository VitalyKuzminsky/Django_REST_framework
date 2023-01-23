import React from 'react'

const ToDoItem = ({todo}) => {
    return (
        <tr>
            <td>
                {todo.project}
            </td>
            <td>
                {todo.text}
            </td>
            <td>
                {todo.created_at}
            </td>
            <td>
                {todo.updated_at}
            </td>
            <td>
                {todo.user}
            </td>
        </tr>
    )
}

const ToDoList = ({todos}) => {
    return (
        <table>
            <th>
                Проект
            </th>
            <th>
                Описание
            </th>
            <th>
                Создан
            </th>
            <th>
                Обновлен
            </th>
            <th>
                Пользователь
            </th>
            {todos.map((todo) => <ToDoItem todo={todo} />)}
        </table>
    )
}

export default ToDoList