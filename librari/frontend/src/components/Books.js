import React from 'react'

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

const BookList = ({books}) => {
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
            {books.map((book) => <BookItem book={book} />)}
        </table>
    )
}

export default BookList