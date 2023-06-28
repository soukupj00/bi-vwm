import {SongCard} from "./index";
import React from "react";

const SongTable = (props) => {
    return (
        <div className="flex justify-center">
            <div className="w-1/2">
                <h2 className="text-white text-3xl font-bold">Found {props.songs.length} songs:</h2>
                <table className="table-auto">
                    <tbody>
                    {props.songs.map((song) => (
                        <tr key={song.id}>
                            <td className="py-2">
                                <SongCard
                                    song={song}
                                />
                            </td>
                        </tr>
                    ))}
                    </tbody>
                </table>
            </div>
        </div>
    );
}

export default SongTable;