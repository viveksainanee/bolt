import React, { Component } from 'react';
import Dashboard from './Dashboard';
import Portal from './Portal';
import { connect } from 'react-redux';
import './BoltApp.css';
import { getUser } from '../actions';
import { withRouter } from 'react-router-dom';

class BoltApp extends Component {
  async componentDidMount() {
    if (localStorage.getItem('currUser')) {
      console.log('currUser in component Did Mount', this.props.currUser);
      await this.props.getUser();
      console.log('this.props in cdm is', this.props);
    }
  }

  componentDidUpdate() {
    console.log('component did update ran');
  }

  render() {
    console.log('curr User is', this.props.currUser);
    return <div>{this.props.currUser ? <Dashboard /> : <Portal />}</div>;
  }
}

function mapStateToProps(state) {
  return { currUser: state.currUser };
}
export default withRouter(
  connect(
    mapStateToProps,
    { getUser }
  )(BoltApp)
);
