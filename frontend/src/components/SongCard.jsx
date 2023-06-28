import {Link} from "react-router-dom";

const SongCard = (props) => {
    return (
        <div className="bg-white rounded-lg shadow-md p-6">
            <div className="card mb-4 shadow-sm">
                <div className="card-body">
                    <h3 className="font-bold text-xl">{props.song.song}</h3>
                    <p className="text-gray-700">
                        {props.song.artist} | {props.song.album} | {props.song.year}
                    </p>

                    <p className="mt-4 text-gray-700">{props.song.lyrics.substring(0, 200)}...</p>
                    <Link
                        to={`songs/${props.song.id}`}
                        className="btn btn-dark btn-block"
                    >
                        <i className="fas fa-chevron-right"/> View Lyrics
                    </Link>
                </div>
            </div>

        </div>
    );
}

export default SongCard;