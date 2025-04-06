
import Image from "next/image";

function Logo() {
  return (
    <Image
      src="/White_Romathery_logo_(Updated).png"
      alt="Romathery logo"
      width={120}
      height={40}
      priority
    />

  );
}

export default Logo;
