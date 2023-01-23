import React from 'react'
import {useParams} from 'react-router-dom'

const BookItem = ({book}) => {
    return (
        <tr>
            <td>
                {book.id}
            </td>
            <td>
                {book.name}
            </td>
            <td>
                {book.author}
            </td>
        </tr>
    )
}

const AuthorBookList = ({books}) => {
    let { id } = useParams()
    let filtered_books = books.filter((book) => book.author.id == id)
    return (
        <table>
            <th>
                ID
            </th>
            <th>
                Название
            </th>
            <th>
                Авторы
            </th>
            {filtered_books.map((book) => <BookItem book={book} />)}
        </table>
    )
}

export default AuthorBookList