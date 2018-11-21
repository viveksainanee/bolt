import React, { Component } from 'react';
import { Switch, Route } from 'react-router-dom';
import Home from './Home';
import Login from './Login';
import SignUp from './SignUp';

class RoutesPortal extends Component {
  constructor(props) {
    super(props);
    this.state = {
      error: [],
      currUser: null
    };
  }

  render() {
    console.log('RoutesPortal Rendered');
    return (
      <div>
        <Switch>
          <Route exact path="/" render={() => <Home />} />
          <Route exact path="/login" render={() => <Login />} />
          <Route exact path="/signup" render={() => <SignUp />} />
        </Switch>
      </div>
    );
  }
}

export default RoutesPortal;
