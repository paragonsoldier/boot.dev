def take_magic_damage(health, resist, amp, spell_power):
    full_damage = spell_power * amp
    damage_taken = full_damage - resist
    return health - damage_taken
