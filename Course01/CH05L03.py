def take_magic_damage(health, resist, amp, spell_power):
    total_maximum_damage = spell_power * amp
    actual_damage = total_maximum_damage - resist
    return health - actual_damage

