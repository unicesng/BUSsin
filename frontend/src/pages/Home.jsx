import SearchBar from "../components/searchbar"
import SchoolBus from "../assets/SchoolBus.gif";

const Home = () => {
    return (
        <>
            <div className="bg-cover bg-center bg-no-repeat h-96 flex flex-col items-center justify-center" style={{ backgroundImage: `url(${SchoolBus})` }}>
                <h1 className="text-black font-semibold mb-10">BUSsin</h1>
                <div className="flex items-center justify-center w-1/2">
                    <SearchBar />
                </div>
            </div>
        </>
    )
}

export default Home