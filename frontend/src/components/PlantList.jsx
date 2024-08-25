import React, { useEffect, useState } from 'react';
import '@mantine/core/styles.css';

const PlantList = () => {
  const [plants, setPlants] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/api/plants/')
      .then(response => response.json())
      .then(data => setPlants(data))
      .catch(error => console.error('Error fetching plants:', error));
  }, []);

  return (
    <div>
      <h1>Plant List</h1>
      <ul>
        {plants.map(plant => (
          <li key={plant.id}>
            <h2>{plant.name}</h2>
            <p>Species: {plant.species}</p>
            <p>Notes: {plant.notes}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default PlantList;
