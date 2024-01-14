import React, {useState} from 'react'
import DeckGL from '@deck.gl/react';
import {BitmapLayer} from '@deck.gl/layers';

const DeckGLComponent = () => {
    const [viewState, setViewState] = useState({
        latitude: 37.7749,
        longitude: -122.4194,
        zoom: 12,
      });
    const layer = [
        new BitmapLayer({
            id: 'bitmap-layer',
            bounds: [-122.5190, 37.7045, -122.355, 37.829],
            image: 'https://raw.githubusercontent.com/visgl/deck.gl-data/master/website/sf-districts.png'
      }),
    ];
    
  return (
    <DeckGL viewState={viewState} layers={layer} />
  )
}

export default DeckGLComponent