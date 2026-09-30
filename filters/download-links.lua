-- Links marked {.dl} render as download badges: [Download](assets/x.pdf){.dl}
function Link(el)
  if el.classes:includes("dl") then
    el.attributes["download"] = ""
    el.attributes["target"] = "_blank"
    return el
  end
end
