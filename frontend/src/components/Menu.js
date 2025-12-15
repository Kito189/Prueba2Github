function Menu({ vista, setVista }) {
  return (
    <nav className="d-flex justify-content-center flex-wrap gap-2">
      <button
        type="button"
        className={`btn ${vista === "ordenes" ? "btn-primary" : "btn-outline-primary"}`}
        onClick={() => setVista("ordenes")}
      >
        Órdenes
      </button>
      <button
        type="button"
        className={`btn ${vista === "facturas" ? "btn-primary" : "btn-outline-primary"}`}
        onClick={() => setVista("facturas")}
      >
        Facturas
      </button>
      <button
        type="button"
        className={`btn ${vista === "envios" ? "btn-primary" : "btn-outline-primary"}`}
        onClick={() => setVista("envios")}
      >
        Envíos
      </button>
    </nav>
  );
}

export default Menu;
