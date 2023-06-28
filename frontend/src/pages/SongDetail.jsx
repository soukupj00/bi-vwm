import React, {Fragment, useEffect, useState} from 'react';
import {Error, Loader} from '../components';
import axios from "axios";
import {useParams} from "react-router-dom";

const SongDetail = () => {
    const [song, setSong] = useState(null)
    const {id} = useParams()

    useEffect(() => {
        axios.get(`http://127.0.0.1:8000/songs/${id}`)
            .then(res => {
                setSong(res.data);
            })
            .catch(err => {
                //Not in the 200 response range
                console.log(err.data);
                console.log(err.status);
                console.log(err.headers);
                return <Error/>;
            });
    }, []);


    if (!song) return <Loader title="Searching for song details"/>;

    return (
        <div className="flex flex-col justify-center items-center">
            <div className="w-1/2 mb-10 text-white p-2">
                <div className="card-body mb-5 ">
                    <h1 className="text-3xl font-bold">{song.artist}</h1>
                    <p className="card-text">
                        <strong>
                            <i className="fas fa-play"/> Song Name
                        </strong>
                        : {song.song}
                        <br/>
                        <strong>
                            <i className="fas fa-compact-disc"/> Album
                        </strong>
                        : {song.album}
                        <strong>
                            <i className="fas fa-compact-disc"/> Year of release
                        </strong>
                        : {song.year}
                    </p>
                </div>
                <h5 className="text-3xl font-bold">Lyrics:</h5>

                <div className="mt-5">
                    {song.lyrics.split('\n').map((line, index) => {
                        return <Fragment key={index}>{line}<br/></Fragment>
                    })}
                </div>
            </div>
        </div>
    );
};

export default SongDetail;
