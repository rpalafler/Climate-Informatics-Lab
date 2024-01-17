import React, { useState } from 'react';
import DeckGL from '@deck.gl/react';
import {CesiumIonLoader} from '@loaders.gl/3d-tiles';
import {Tile3DLayer} from '@deck.gl/geo-layers';
//CODE MODIFIED FROM DECK.GL DOCUMENTATION: https://deck.gl/docs/api-reference/geo-layers/tile-3d-layer

const DeckGLComponent = () => {
    const [viewState, setViewState] = useState({
        latitude: 37.7749,
        longitude: -122.4194,
        zoom: 12,
      });
      const layer = new Tile3DLayer({
        id: 'tile-3d-layer',
        // tileset json file url
        data: 'https://assets.cesium.com/43978/tileset.json',
        loader: CesiumIonLoader,
        // https://cesium.com/docs/rest-api/
        loadOptions: {
          'cesium-ion': {accessToken: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJlNTZlMzU4OC0yZjEzLTQ0NmMtYWI4OC0xY2Q1ZTIxZjBkYTUiLCJpZCI6MTg3MTE5LCJpYXQiOjE3MDM5ODA0NjF9.WmjpO2msItlK2FZV0mQHm4f4cOeZQCAKWmmIEHvL6Uo'}
        },
        onTilesetLoad: (tileset) => {
          // Recenter to cover the tileset
          const {cartographicCenter, zoom} = tileset;
          this.setState({
              viewState: {
                ...this.state.viewState,
                longitude: cartographicCenter[0],
                latitude: cartographicCenter[1],
                zoom
              }
          });
        },
        // override scenegraph subLayer prop
        _subLayerProps: {
          scenegraph: {_lighting: 'flat'}
        }
      });
  return ( 
  <DeckGL viewState={viewState} layers={layer} />
  )
}

export default DeckGLComponent