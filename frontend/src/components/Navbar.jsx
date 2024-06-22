import BUSsinLogo from "../assets/BUSsinLogo.png";

const Navbar = () => {
  return (
    <nav className="border-gray-200 w-full flex items-center">
      <div className="flex items-center">
        <img src={BUSsinLogo} alt="BUSsin Logo" width="100" />
      </div>
    </nav>
  );
};

export default Navbar;