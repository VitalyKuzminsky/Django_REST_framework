import React from 'react'
import {Link} from 'react-router-dom'

const ToDoItem = ({todo, deleteTodo}) => {
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
            <td>
                <button onClick={()=>deleteTodo(todo.id)} type='button'>
                    Delete
                </button>
            </td>
        </tr>
    )
}

const ToDoList = ({todos, deleteTodo}) => {
    return (
        <div>
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
                {todos.map((todo) => <ToDoItem todo={todo} deleteTodo={deleteTodo} />)}
                <Link to='/todo/create'>Create</Link>
            </table>
        </div>
    )
}

export default ToDoList