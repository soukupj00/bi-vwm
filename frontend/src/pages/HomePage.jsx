import React from 'react';
import {Loader} from '../components';
import SongTable from "../components/SongTable";


const HomePage = (props) => {
    if (!props.songs) return <Loader title="Waiting for search term"/>;

    return (
        <div className="flex flex-col justify-center items-center">
            <div className="mb-10">
                {props.songs.length > 0 ?
                    <SongTable songs={props.songs}/>
                    :
                    <h2 className="text-white text-3xl font-bold">No songs found</h2>
                }
            </div>
        </div>

    );
};

export default HomePage;
