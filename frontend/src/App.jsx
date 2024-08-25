import React from 'react';
import PlantList from './components/PlantList';
import Home from "./pages/homePage";
import PlantPage from "./pages/plantPage";

import { BrowserRouter as Router, Route, Routes, Link, useNavigate } from 'react-router-dom';

import '@mantine/core/styles.css';
import { createTheme, MantineProvider, AppShell, Button } from '@mantine/core';

function App() {

  const theme = createTheme({
    fontFamily: 'Verdana, sans-serif',
    defaultRadius: 'md',
    primaryColor: 'main-green',
    colors: {
      'bright-pink': ['#F0BBDD', '#ED9BCF', '#EC7CC3', '#ED5DB8', '#F13EAF', '#F71FA7', '#FF00A1', '#E00890', '#C50E82', '#AD1374'],
      'fun_green': [
        '#7b9c8d',
        '#93c9b1',
        '#347859',
        '#2e3630',
      ],
      'background': ["#e7edde"],
      'main-green': ['#1B4723', '#1B4723', '#1B4723', '#1B4723', '#1B4723', '#1B4723', '#1B4723', '#1B4723', '#1B4723', '#1B4723'],
    },
  });

  return (
    <MantineProvider theme={theme}>
      <AppShell header={{ height: { base: 48, sm: 60, lg: 76 } }}
        styles={(theme) => ({
          header: { backgroundColor: theme.colors['main-green'][0] }, 
          footer: { backgroundColor: theme.colors['main-green'][0] }, 
        })}>
        <AppShell.Header style={{ color: 'rgb(231, 237, 222)' }} p="xs">bloom!</AppShell.Header>
        <AppShell.Footer p="xs"></AppShell.Footer>
        <div className="App"
          style={{
            height: '100vh',
            width: '100%',
            backgroundColor: theme.colors['background'][0],
          }}>
          <main style={{ flex: 1, paddingTop: '120px' }}>
            <Router>
              <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/plantPage" element={<PlantPage />} />
              </Routes>
            </Router>
          </main>
        </div>
      </AppShell>
    </MantineProvider>
  );
}

export default App;
