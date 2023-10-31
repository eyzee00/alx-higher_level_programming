#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - inserts a node in a sorted linked list, the sort is
 * taken by consideration
 * @head: the address of the pointer to the head of the list
 * @number: data contained within the new node
 * Return: address of the new node or NULL if allocation failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode = NULL, *iter = *head;

	newnode = malloc(sizeof(listint_t));
	if (newnode == 0)
		return (NULL);
	newnode->n = number;
	if (number < iter->n || iter == NULL)
	{
		newnode->next = iter;
		*head = newnode;
		return (newnode);
	}
	while (iter->next != NULL && number > iter->next->n)
		iter = iter->next;
	newnode->next = iter->next;
	iter->next = newnode;
	return (newnode);
}
