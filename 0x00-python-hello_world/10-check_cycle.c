#include "lists.h"

/**
 * check_cycle - checks if the given linked list has a cycle in it
 * Using "army" and "scouts" metaphor(the army and scouts start from
 * the same position. The scouts move twice faster than
 * the army, if there is a cycle in the list, the scout will
 * eventually end up meeting with the army again which is only
 * possible if there is a cycle in the list)
 * @list: a pointer to the head of the list
 * Return: (1) if there is a cycle, (2) if there is no cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *army, *scouts;

	army = list;
	scouts = list;
	while (scouts != 0x0 && scouts->next != 0x0)
	{
		army = army->next;
		scouts = scouts->next->next;
		if (army == scouts)
			return (1);
		continue;
	}
	return (0);
}
