import React, { Component } from 'react';
import Add from './Add.js';
import { StackNavigator } from 'react-navigation';
export default (DrawNav = StackNavigator(
{
  Add: { screen: Add }
}));