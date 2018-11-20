import React, { Component } from 'react';
import { Switch, Route } from 'react-router-dom';
import Home from './Home';
import Login from './Login';
import GetStarted from './GetStarted';
import SignUp from './SignUp';

class Routes extends Component {
  constructor(props) {
    super(props);
    this.state = {
      error: [],
      currUser: null
    };
  }

  render() {
    return (
      <div>
        <Switch>
          <Route exact path="/" render={() => <Home />} />
          <Route exact path="/login" render={() => <Login />} />
          <Route exact path="/getstarted" render={() => <GetStarted />} />
          <Route exact path="/signup" render={() => <SignUp />} />
        </Switch>
      </div>
    );
  }
}

export default Routes;
