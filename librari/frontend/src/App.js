import React from 'react';
import axios from 'axios'
import logo from './logo.svg';
import './App.css';
import AuthorList from './components/Author.js'
import UserList from './components/User.js'
import BookList from './components/Books.js'
import AuthorBookList from './components/AuthorBook.js'
import {HashRouter, BrowserRouter, Route, Link, Switch, Redirect} from 'react-router-dom'

const NotFound404 = ({ location }) => {
    return (
        <div>
            <h1>
                Страница по адресу `{location.pathname}` не найдена
            </h1>
        </div>
    )
}

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'authors': [],
            'users': [],
            'books': []
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/authors/')
            .then(response => {
                const authors = response.data
                    this.setState(
                    {
                        'authors': authors
                    }
                )
        }).catch(error => console.log(error))
        axios.get('http://127.0.0.1:8000/api/users/')
            .then(response => {
                const users = response.data
                    this.setState(
                    {
                        'users': users
                    }
                )
        }).catch(error => console.log(error))
        axios.get('http://127.0.0.1:8000/api/books/')
            .then(response => {
                const books = response.data
                    this.setState(
                    {
                        'books': books
                    }
                )
        }).catch(error => console.log(error))
    }

    render () {
        return (
            <div className='App'>
                <BrowserRouter>
                    <nav>
                        <ul class='App-link'>
                            <li>
                                <Link to='/'>Авторы</Link>
                            </li>
                            <li>
                                <Link to='/books'>Книги</Link>
                            </li>
                            <li>
                                <Link to='/users'>Пользователи</Link>
                            </li>
                        </ul>
                    </nav>

                    <Switch>
                        <Route exact path='/' component={() => <AuthorList authors={this.state.authors} />} />
                        <Route exact path='/books' component={() => <BookList books={this.state.books} />} />
                        <Route exact path='/users' component={() => <UserList users={this.state.users} />} />
                        <Route exact path='/author/:id' component={() => <AuthorBookList books={this.state.books} />} />
                        <Redirect from='/authors' to='/' />
                        <Route component={NotFound404} />
                    </Switch>
                </BrowserRouter>
            </div>
        )
    }
}

export default App;
