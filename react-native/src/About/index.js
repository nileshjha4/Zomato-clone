import React, { Component } from 'react';
import About from './About.js';
import { StackNavigator } from 'react-navigation';
export default (DrawNav = StackNavigator(
{
  About: { screen: About }
}));