import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link, useNavigate } from 'react-router-dom';
import { Button, Group, Stack } from '@mantine/core';

function Home() {

    const navigate = useNavigate();

    const handleGetStartedClick = () => {
        navigate('/plantPage'); 
    };

    return(
        <Group justify="center">
            <Stack align="center" gap="xl">
                <h1 style={{ color: 'rgb(27, 71, 35)' }}>Welcome to bloom, your plant care companion.</h1>
                <Button 
                    variant="gradient" 
                    size="xl" 
                    gradient={{ from: 'rgba(1, 82, 25, 1)', to: 'rgba(110, 110, 110, 1)', deg: 90 }}
                    onClick={handleGetStartedClick}
                >
                    Get Started</Button>
            </Stack>
        </Group>
    );
}

export default Home;

