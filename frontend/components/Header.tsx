import Logo from "./Logo";


function Header() {
  return (
    <header className="w-full bg-primary shadow sticky top-0 z-50">
      <div className="max-w-[1200px] mx-auto flex items-center justify-between p-4">
        <Logo/>
        {/* You can add nav or buttons here later */}
      </div>
    </header>
  );
}

export default Header;
