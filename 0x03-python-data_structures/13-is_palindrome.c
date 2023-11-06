#include "lists.h"
/**
 * is_palindrome - checks if a linked list is palindrome
 * @head: the address of the pointer to the head of the list
 * Return: 0 if not palindrome, 1 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *army = *head, *scouts = *head;
	listint_t *campfire = NULL, *backstep = NULL;
	listint_t *top, *bottom;

	if (army == NULL || head == NULL)
		return (1);
	while (scouts != 0 && scouts->next != 0)
	{
		scouts = scouts->next->next;
		army = army->next;
	}
	while (army != 0)
	{
		campfire = army->next;
		army->next = backstep;
		backstep = army;
		army = campfire;
	}
	top = *head;
	bottom = backstep;
	while (bottom != 0)
	{
		if (bottom->n != top->n)
			return (0);
		bottom = bottom->next;
		top = top->next;
	}
	return (1);
}
