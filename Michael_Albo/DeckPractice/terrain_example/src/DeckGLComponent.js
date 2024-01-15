import React, {useState} from 'react';
import DeckGL from 'deck.gl';
import {TerrainLayer} from '@deck.gl/geo-layers';
//CODE MODIFIED FROM DECK.GL DOCUMENTATION: https://deck.gl/docs/api-reference/geo-layers/terrain-layer

const DeckGLComponent = () => {
    const [viewState, setViewState] = useState({
        latitude: 37.7749,
        longitude: -122.4194,
        zoom: 12,
      });
    
      const layer = new TerrainLayer({
        elevationDecoder: {
          rScaler: 2,
          gScaler: 0,
          bScaler: 0,
          offset: 0
        },  elevationData: 'https://raw.githubusercontent.com/visgl/deck.gl-data/master/website/terrain.png',
        texture: 'https://raw.githubusercontent.com/visgl/deck.gl-data/master/website/terrain-mask.png',
        bounds: [-122.5233, 37.6493, -122.3566, 37.8159],
      });
    
  return (
    <DeckGL viewState = {viewState} layers={layer} />
  )
}

export default DeckGLComponent;