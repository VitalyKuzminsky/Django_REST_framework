import React from 'react';
import axios from 'axios'
//import logo from './logo.svg';
import './App.css';
import AuthorList from './components/Author.js'
import BookList from './components/Books.js'
import AuthorBookList from './components/AuthorBook.js'
import UserList from './components/User.js'
import ProjectList from './components/Projects.js'
import ToDoList from './components/ToDo.js'
import LoginForm from './components/Auth.js'
import {BrowserRouter, Route, Link, Switch, Redirect} from 'react-router-dom'
import Cookies from 'universal-cookie';


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
            'books': [],
            'users': [],
            'projects': [],
            'todos': [],
            'token': ''
        }
    }

    set_token(token) {
        const cookies = new Cookies()
        cookies.set('token', token)
        localStorage.setItem('token', token)
        this.setState({'token': token}, () => this.load_data())
    }

    is_authenticated() {
        return this.state.token != ''
    }

    logout() {
        this.set_token('')
    }

    get_token_from_storage() {
        const cookies = new Cookies()
//        const token = cookies.get('token')
        const token = localStorage.getItem('token')
        this.setState({'token': token}, () => this.load_data())
    }

    get_token(login, password) {
        axios.post('http://127.0.0.1:8000/api-token-auth/', {'username': login, 'password': password})
            .then(response => {
                this.set_token(response.data['token'])
            }).catch(error => alert('Неверный логин или пароль'))
    }

    get_headers() {
        let headers = {
            'Content-Type': 'application/json',
        }
        if (this.is_authenticated()) {
            headers['Authorization'] = 'Token ' + this.state.token
        }
        return headers
    }

    load_data() {
        const headers = this.get_headers()
        axios.get('http://127.0.0.1:8000/api/authors/', headers)
            .then(response => {
                const authors = response.data
                    this.setState(
                    {
                        'authors': authors['results']
                    }
                )
        }).catch(error => console.log(error))
        axios.get('http://127.0.0.1:8000/api/books/', headers)
            .then(response => {
                const books = response.data
                    this.setState(
                    {
                        'books': books['results']
                    }
                )
        }).catch(error => console.log(error))
        axios.get('http://127.0.0.1:8000/api/users/', headers)
            .then(response => {
                const users = response.data
                    this.setState(
                    {
                        'users': users['results']
                    }
                )
        }).catch(error => console.log(error))
        axios.get('http://127.0.0.1:8000/api/project/', headers)
            .then(response => {
                const projects = response.data
                    this.setState(
                    {
                        'projects': projects['results']
                    }
                )
        }).catch(error => console.log(error))
        axios.get('http://127.0.0.1:8000/api/todo/', headers)
            .then(response => {
                const todos = response.data
                    this.setState(
                    {
                        'todos': todos['results']
                    }
                )
        }).catch(error => console.log(error))
    }

    componentDidMount() {
        this.get_token_from_storage()
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
                            <br/>
                            <li>
                                <Link to='/users'>Пользователи</Link>
                            </li>
                            <li>
                                <Link to='/projects'>Проекты</Link>
                            </li>
                            <li>
                                <Link to='/todos'>ToDo</Link>
                            </li>
                            <br/>
                            <li>
                                {this.is_authenticated() ? <button onClick={() => this.logout()}>Logout</button> :
                                <Link to='/login'>Login</Link>}
                            </li>
                        </ul>
                    </nav>

                    <Switch>
                        <Route exact path='/' component={() => <AuthorList authors={this.state.authors} />} />
                        <Route exact path='/books' component={() => <BookList books={this.state.books} />} />
                        <Route exact path='/users' component={() => <UserList users={this.state.users} />} />
                        <Route exact path='/projects' component={() => <ProjectList projects={this.state.projects} />} />
                        <Route exact path='/todos' component={() => <ToDoList todos={this.state.todos} />} />
                        <Route exact path='/author/:id' component={() => <AuthorBookList books={this.state.books} />} />
                        <Route exact path='/login' component={() => <LoginForm
                            get_token={(login, password) => this.get_token(login, password)}/>} />
                        <Redirect from='/authors' to='/' />
                        <Route component={NotFound404} />
                    </Switch>
                </BrowserRouter>
            </div>
        )
    }
}

export default App;
