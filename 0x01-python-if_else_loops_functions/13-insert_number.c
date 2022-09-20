#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: The address of the head of the sorted singly linked list.
 * @number: The number to be inserted.
 * Return: the address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new, *prev = NULL;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;
	if (current == NULL)
	{
		*head = new;
		return (new);
	}
	if (number <= current->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	prev = current;
	current = current->next;

	while (current)
	{
		if (number <= current->n)
		{
			prev->next = new;
			new->next = current;
			break;
		}
		prev = current;
		current = current->next;
	}
	if (new->next == NULL)
		prev->next = new;
	return (new);
}
