
import Logo from "./Logo";

function Footer() {
  return (
    <footer className="bg-primary text-gray-100">
      <div className="max-w-[1200px] mx-auto px-4 py-8 grid grid-cols-1 md:grid-cols-2 gap-6">
        {/* Branding */}
        <div>
          <Logo />
          <p className="text-sm">Built for vendors in Nigeria 🇳🇬</p>
        </div>

        {/* Navigation Links */}
        {/* <div>
          <h3 className="text-md font-semibold mb-2">Navigation</h3>
          <ul className="space-y-1 text-sm">
            <li>
              <Link href="/" className="hover:underline">Home</Link>
            </li>
            <li>
              <Link href="/about" className="hover:underline">About</Link>
            </li>
            <li>
              <Link href="/products" className="hover:underline">Products</Link>
            </li>
            <li>
              <Link href="/contact" className="hover:underline">Contact</Link>
            </li>
          </ul>
        </div> */}

        {/* Contact Info or Placeholder */}
        <div className="md:flex md:justify-end">
          <div>
            <h3 className="text-md font-semibold mb-2">Contact</h3>
            <p className="text-sm">Email: support@romathery.com</p>
            <p className="text-sm">Phone: +234 800 123 4567</p>
            <p className="text-sm">Address: 10/11 Sabbath church close, Ijesha-tedo, Lagos, Nigeria</p>
          </div>
        </div>
      </div>

      <div className="text-center py-4 text-sm bg-base-300 text-base-content">
        &copy; {new Date().getFullYear()} Romathery. All rights reserved.
      </div>
    </footer>
  );
}

export default Footer;
