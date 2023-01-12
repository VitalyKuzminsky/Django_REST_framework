import React from 'react';
import axios from 'axios'
import logo from './logo.svg';
import './App.css';
import AuthorList from './components/Author.js'
import UserList from './components/User.js'


class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'authors': [],
            'users': []
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
    }

    render () {
        return (
            <div class='App-header App'>
                <div>
                    Блок меню
                    <hr/>
                </div>
                <div>
                    <br/>
                    Это код с урока 2:
                    <AuthorList authors={this.state.authors} />
                </div>
                <div>
                    <br/>
                    Это код из ДЗ 2:
                    <UserList users={this.state.users} />
                </div>
                <div>
                    <hr/>
                    Блок футер
                </div>
            </div>
        )
    }
}

export default App;
