import React, { useState } from 'react';
import DeckGL from 'deck.gl';
import { ScatterplotLayer } from '@deck.gl/layers';

const DeckGLComponent = () => {
  const [viewState, setViewState] = useState({
    latitude: 37.7749,
    longitude: -122.4194,
    zoom: 12,
  });

  const layers = [
    new ScatterplotLayer({
      id: 'scatter-plot',
      data: [{ position: [-122.4194, 37.7749], size: 100 }],
      getPosition: (d) => d.position,
      getRadius: (d) => d.size,
    }),
  ];

  return <DeckGL viewState={viewState} layers={layers} />;
};

export default DeckGLComponent;